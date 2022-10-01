import { Component } from '@angular/core';
import { EChartsOption } from 'echarts';
import { ApiService } from './api.service';
import { Order } from './order';
import { WebsocketService } from './websocket';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  orders: Array<Order> = [];

  chartOption: EChartsOption = {
    xAxis: {
      type: 'category',
      data: [],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        data: [],
        type: 'line',
      },
    ],
  };

  ordering = 'id';
  reversed = true;

  constructor(public api: ApiService, public ws: WebsocketService){
    api.getOrders().subscribe((data: any) => {
      this.orders = data;
      this.updateCharData();
      this.sortData();
    })

    ws.on('order-deleted').subscribe((id: any) => {
      console.log('order-deleted', id);
      for(var i = 0; i < this.orders.length; i++){
        if(this.orders[i].id == id){
          this.orders.splice(i, 1);
          this.updateCharData();
          break;
        }
      }
    });
    
    ws.on('order-created').subscribe((order: any) => {
      console.log('order-created', order);
      this.orders.push(order);
      this.updateCharData();
      this.sortData();
    })
    
    ws.on('order-updated').subscribe((order: any) => {
      console.log('order-updated', order);
      for(var i = 0; i < this.orders.length; i++){
        if(this.orders[i].id == order.id){
          this.orders[i] = order;
          this.updateCharData();
          this.sortData();
          break;
        }
      }
    });
  }

  setOrdering(by: string){
    if(by == this.ordering){
      this.reversed = !this.reversed;
    } else {
      this.ordering = by;
      this.reversed = false;
    }
    this.sortData();
  }

  sortData(){
    this.orders.sort((a, b) => {
      var result;
      if(this.ordering == 'id'){
        result = a.id - b.id;
      } else if(this.ordering == 'orderId'){
        result = a.orderId - b.orderId;        
      } else if(this.ordering == 'cost'){
        result = a.cost - b.cost;
      } else if(this.ordering == 'costInRubles'){
        result = a.cost - b.cost;
      } else {
        result = new Date(a.deliveryTime).valueOf() - new Date(b.deliveryTime).valueOf();
      }
      if(this.reversed){
        result = -result;
      }
      return result;
    });
  }

  updateCharData(){
    var data = new Map<string, number>();
    var orders = this.orders.copyWithin(0, this.orders.length);
    orders.sort((a, b) => {
      return new Date(a.deliveryTime).valueOf() - new Date(b.deliveryTime).valueOf();
    });
    for(let order of orders){
      var key = order.deliveryTime.toString();
      data.set(key, data.get(key)||0 + order.cost);
    }
    var keys = [];
    var values = [];
    for(let key of data.keys()){
      keys.push(key);
    }
    for(let value of data.values()){
      values.push(value);
    }
    this.chartOption = {
      xAxis: {
        type: 'category',
        data: keys,
      },
      yAxis: {
        type: 'value',
      },
      series: [
        {
          data: values,
          type: 'line',
        },
      ],
    };
  }
}
