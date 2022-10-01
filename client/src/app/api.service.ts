import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  BASE_API_URL = environment.api_url;

  constructor(
    private http: HttpClient,
  ) { }

  get(prefix: string, params: any = {}, otherOptions: any = {}) {
    let url = this.BASE_API_URL + prefix;
    let options = otherOptions;
    options.params = params;

    options.headers = new HttpHeaders();

    options.headers = options.headers.set('Content-Type', 'application/json');
    options.withCredentials = true;

    return this.http.get(url, options);
  }

  getOrders(){
    return this.get('order');
  }
}
