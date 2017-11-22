import { Component, OnInit, Input } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
   selector: 'app-root',
    templateUrl: './app.component.html',
   //template:`{{ title }} is cool`,  // ticks.. not quotes
   styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
   title = 'Trips';

    private routeSub:any;
    query: string;
    // @Input()
    // passedQuery:string;
    // searchedQuery:string;

  constructor(private route:ActivatedRoute ) {
      this.query="";
  }

   ngOnInit() {
      this.routeSub=this.route.params.subscribe(params=>{
          console.log(params)
          this.query=params['q']
      })
  }
  ngOnDestroy(){
      this.routeSub.unsubscribe()
  }


}
