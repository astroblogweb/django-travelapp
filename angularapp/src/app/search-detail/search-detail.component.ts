import { Component, OnInit, OnDestroy, ViewEncapsulation } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {TripService} from '../trips/trips.service';
import { TripItem } from '../trips/trip';

@Component({
  selector: 'app-search-detail',
  templateUrl: './search-detail.component.html',
  styleUrls: ['./search-detail.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers:[TripService]
})
export class SearchDetailComponent implements OnInit,OnDestroy {
    private routeSub:any;
    query:any;
    private req:any;
    triplist:[TripItem];
  constructor(private route:ActivatedRoute, private _trip:TripService) { }

  ngOnInit() {
      this.routeSub=this.route.params.subscribe(params=>{
          console.log(params)
          this.query=params['q']
        this.req=this._trip.search(this.query).subscribe(data=>{
        this.triplist=data as [TripItem];    // data is output of 'filter' => its an array, not json
        console.log("in search detail comp: triplist: ",this.triplist)
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
