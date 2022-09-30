import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

export class Error{
  constructor(
    public me:number,
    public mae:number,
    public rmse:number,
    public mape:number,
    public u1:number,
    // public u2:number
  ){}
}


@Component({
  selector: 'app-predict-page',
  templateUrl: './predict-page.component.html',
  styleUrls: ['./predict-page.component.css']
})
export class PredictPageComponent implements OnInit {

  errors : Error[] | undefined

  constructor(
    private httpClient : HttpClient
  ) { }
  ngOnInit(): void {

    this.getError();
    
  }

  getError(){
    this.httpClient.get<any>('http://localhost:5000/api/predict').subscribe(
      response => {
        console.log(response);
        this.errors = response;
      });
      }
  }
  
// import {Component} from '@angular/core';

// export interface PeriodicElement {
//   name: string;
//   position: number;
//   weight: number;
//   symbol: string;
// }

// const ELEMENT_DATA: PeriodicElement[] = [
//   {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
//   {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
//   {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
//   {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
//   {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
//   {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
//   {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
//   {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
//   {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
//   {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
// ];

// /**
//  * @title Table with columns defined using ngFor instead of statically written in the template.
//  */
// @Component({
//   selector: 'app-predict-page',
//   templateUrl: './predict-page.component.html',
//   styleUrls: ['./predict-page.component.css']
// })
// export class PredictPageComponent {
//   columns = [
//     {
//       columnDef: 'position',
//       header: 'No.',
//       cell: (element: PeriodicElement) => `${element.position}`,
//     },
//     {
//       columnDef: 'name',
//       header: 'Name',
//       cell: (element: PeriodicElement) => `${element.name}`,
//     },
//     {
//       columnDef: 'weight',
//       header: 'Weight',
//       cell: (element: PeriodicElement) => `${element.weight}`,
//     },
//     {
//       columnDef: 'symbol',
//       header: 'Symbol',
//       cell: (element: PeriodicElement) => `${element.symbol}`,
//     },
//   ];
//   dataSource = ELEMENT_DATA;
//   displayedColumns = this.columns.map(c => c.columnDef);
// }
