import { Component, OnInit, OnDestroy, ViewEncapsulation } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';

// after TripService
// import { HttpClientModule } from '@angular/common/http';
// import { HttpModule } from '@angular/http';
// import {Http} from '@angular/http';

import { TripItem } from '../trips/trip';
import {TripService} from '../trips/trips.service';


@Component({
  selector: 'trip-list',
  templateUrl: './trip-list.component.html',
  styleUrls: ['./trip-list.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers:[TripService]
})
export class TripListComponent implements OnInit,OnDestroy {
    private req:any;
    bgcolor: any;
    title="Places of Interest";
    something="<h1>something</h1>";
    todayDate;
    triplistitems:[TripItem]; // array of ANY type
    // triplistitems=["item 1", "item 2", "item 3"]
    // triplistitems=[ // json i.e.dic
    //     {name:"item 1", slug:"item-1",embed:`6wD4V0rvlDI`},
    //     {name:"item 2", slug:"item-2",embed:`lYvmbQiFnXE`},
    //     {name:"item 3", slug:"item-3",embed:`LOJJvMacqEg`}
    // ]
  //constructor(private sanitizer:DomSanitizer) { }

  // before TripService
  //constructor(private http:Http,private _trip:TripService) { }
  //after TripService
  constructor(private _trip:TripService,private sanitizer:DomSanitizer) { }

  ngOnInit() { this.todayDate=new Date()

// // before TripService   // constructor(private http:Http,private _trip:TripService) { }
//     this.req=this.http.get('assets/json/trips.json').subscribe(data=>{
//       console.log(data.json())
//       this.triplistitems=data.json() as [any];
//     })


   // after TripService
      this.req=this._trip.list().subscribe(data=>{
        console.log(data)
        this.triplistitems=data as [TripItem];
      })


   // after API-getdinos--- works.. b4 listplaces
      this.req=this._trip.listTrips()
      .then(data=>{ console.log(data); this.triplistitems=data as [TripItem];})
      .catch(error=>{console.log(error)})


     // this.req=this._trip.listPlaces().subscribe(data=>{
     //      // this.trip=data as TripItem
     //      console.log("list places in trip list comp :", data)
     //  })


      //   // 'search' TripService   -  works
      // this.req=this._trip.search("item 3").subscribe(data=>{
      //   console.log(data)
      //   this.triplistitems=data as [any];
      // })



   }




  ngOnDestroy(){

    // this.req.unsubscribe()  // needed only when 'subscribe' is used
  }


  getEmbedURL(item){
    return 'https://www.youtube.com/embed/'+item.embed+'?ecver=2'
  }

  getColor(item){
    if (item.site_category=="Bridges"){
      // console.log("city:jaipur, red")
      return ("#EDBB99")
    }
    if (item.site_category=="Zoos"){
      // console.log("city:udaipur, green")
      return ("#FADBD8")
    }
    if (item.site_category=="Caverns & Caves"){
      // console.log("city:udaipur, green")
      return ("#D5DBDB")
    }
    if (item.site_category=="Sacred & Religious Sites"){
      // console.log("city:udaipur, green")
      return ("#FCF3CF")
    }
    if (item.site_category=="Military Museums"){
      // console.log("city:udaipur, green")
      return ("#AEB6BF")
    }
    if (item.site_category=="Mountains"){
      // console.log("city:udaipur, green")
      return ("#27ae60")
    }
    if (item.site_category=="Valleys"){
      // console.log("city:udaipur, green")
      return ("#A9DFBF")
    }
    if (item.site_category=="Parks"){
      // console.log("city:udaipur, green")
      return ("#16A085")
    }
    if (item.site_category=="Historic Sites"){
      // console.log("city:udaipur, green")
      return ("#D7BDE2")
    }
    if (item.site_category=="Beaches"){
      // console.log("city:udaipur, green")
      return ("#85C1E9")
    }
    if (item.site_category=="Educational sites"){
      // console.log("city:udaipur, green")
      return ("#F2D7D5  ")
    }
    if (item.site_category=="Points of Interest & Landmarkss"){
      // console.log("city:udaipur, green")
      return ("#F5B7B1")
    }
    else{
      // console.log("city:.., black")
      return ("#ffffff")
    }


  }

  private safe_bgcolor(color){this.bgcolor = this.sanitizer.bypassSecurityTrustStyle(color);}
}


