import { Component, OnInit, OnDestroy, ViewEncapsulation } from '@angular/core';
import {Router} from '@angular/router';
import {Http} from '@angular/http';
import { TripItem } from '../trips/trip';
import {TripService} from '../trips/trips.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers:[TripService]
})
export class HomeComponent implements OnInit, OnDestroy {
    // prevented=false;
    private req: any;
    homeImageList:[TripItem] = [] as [TripItem]

  constructor(private http:Http,private router:Router,private _trip:TripService) { }

    ngOnInit() {
        this.req=this._trip.list().subscribe(data=>{
             data.filter(item=>{
                   if (item.featured){
                     let dataitem=item
                     this.homeImageList.push(dataitem)
                   }
             })

        })
      }

      ngOnDestroy(){

      }

  preventNormal(event:MouseEvent, image:any){
      if (!image.prevented){
      // event.preventDefault()
      // // console.log("in prevent normal")
      // image.link='/trips' // if interested in over-writing the parameter.. image.link
      // image.prevented=true
      // this.router.navigate(['./trips'])
      }




  }
}
