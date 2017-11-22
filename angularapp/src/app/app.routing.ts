import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import { TripListComponent } from './trip-list/trip-list.component';
import { TripDetailComponent } from './trip-detail/trip-detail.component';
import { HomeComponent } from './home/home.component';
import { SearchDetailComponent } from './search-detail/search-detail.component';

const appRoutes: Routes = [
    {path:"",component:HomeComponent}, // home
    {path:"trips",component:TripListComponent},
    {path:"trips/:slug",component:TripDetailComponent},
    {path:"search",component:SearchDetailComponent}
    // {path:"trips/:slug/:abc/:xyz",component:TripDetailComponent}
]



@NgModule({
    imports:[ RouterModule.forRoot(appRoutes)    ],
    exports: [  RouterModule  ]
})
export class AppRoutingModule{}