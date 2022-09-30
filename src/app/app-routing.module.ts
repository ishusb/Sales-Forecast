import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginPageComponent } from './login-page/login-page.component';
import { UserPageComponent } from './user-page/user-page.component';
import { PredictPageComponent } from './predict-page/predict-page.component';
const routes: Routes = [
  {
    path:'user',
    component:UserPageComponent
  },
  {
    path:'',
    component:LoginPageComponent
  },
  {
    path:'predict',
    component:PredictPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
