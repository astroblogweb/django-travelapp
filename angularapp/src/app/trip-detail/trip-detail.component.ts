import { Component, OnInit, ViewEncapsulation, OnDestroy } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
// import {Http} from '@angular/http';
import {TripService} from '../trips/trips.service';
import { TripItem } from '../trips/trip';

@Component({
  selector: 'trip-detail',
  templateUrl: './trip-detail.component.html',
  styleUrls: ['./trip-detail.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers:[TripService]

})
export class TripDetailComponent implements OnInit, OnDestroy {
    private routeSub:any;
    private req:any;
        slug:string;
        trip:TripItem;


// after TripService's new: get()
  constructor(private route:ActivatedRoute,private _trip:TripService) { }
  ngOnInit() {
      this.routeSub=this.route.params.subscribe(params =>{
          // console.log(params)
        this.slug=params['slug']
        console.log("site_slug:", this.slug)

        this.req=this._trip.detailTrips(this.slug).subscribe(data=>{
          this.trip=data as TripItem
          console.log("this.trip :", this.trip)
        })

      })
  }

  ngOnDestroy(){
      this.routeSub.unsubscribe()
      this.req.unsubscribe()

  }
  getEmbedURL(item){
    return 'https://www.youtube.com/embed/'+item.embed+'?ecver=2'
  }
}

// // after TripService
//   constructor(private route:ActivatedRoute,private _trip:TripService) { }
//   ngOnInit() {
//       this.routeSub=this.route.params.subscribe(params =>{
//           console.log(params)
//         this.slug=params['slug']
//         this.req=this._trip.list().subscribe(data=>{
//             data.filter(item=>{
//               if(item.slug==this.slug){
//                 console.log(item)
//                 this.trip=item
//               }
//             })
//         })
//       })
//   }

// // before TripService
//   constructor(private route:ActivatedRoute, private http:Http) { }
//   ngOnInit() {
//       this.routeSub=this.route.params.subscribe(params =>{
//           console.log(params)
//         this.slug=params['slug']
//         this.req=this.http.get('assets/json/trips.json').subscribe(data=>{
//             data.json().filter(item=>{
//               if(item.slug==this.slug){
//                 console.log(item)
//                 this.trip=item
//               }
//             })
//         })
//       })
//   }



