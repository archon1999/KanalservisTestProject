export class Order {
    constructor(
        public id: number,
        public orderId: number,
        public cost: number,
        public costInRubles: number,
        public deliveryTime: Date
    ){}

    static fromJSON(data: any){
        return new Order(
            data.id,
            data.orderId,
            data.cost,
            data.costInRubles,
            new Date(data.delivertTime)
        )
    }
}
