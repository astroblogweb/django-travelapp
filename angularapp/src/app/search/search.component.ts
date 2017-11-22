import { Component, OnInit, ViewEncapsulation, Input } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class SearchComponent implements OnInit {
    searchlocation="default_loc"
    searchQuery:string;
    @Input()
    passedQuery:string;
    q:string;

  constructor(private router:Router) {
  }

  ngOnInit() {
    console.log(this.passedQuery)
    if (this.passedQuery){
      this.searchQuery=this.passedQuery
    }
  }
  submitSearch(event,formData){
      console.log(event)
      console.log(formData.value)
      let searchQuery=formData.value['q'] // was ['searchQuery']
      if (searchQuery){
          this.router.navigate(['/search',{q:searchQuery}]) // array: [link, {params}]
      }

  }
  searchlocationchange(){
      this.searchlocation="changed_loc"
  }
}
