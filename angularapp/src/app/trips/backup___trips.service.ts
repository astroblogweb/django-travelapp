import { Injectable } from '@angular/core';
import {Http} from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

const endpoint='assets/json/trips.json'

@Injectable()
export class TripService {

  constructor(private http:Http) { }

  private handleError(error:any, caught:any):any{
          console.log(error,caught)
  }

  list(){
      return this.http.get(endpoint)   // to avoid needing to subscribe/unsubscribe:use map+catch
              .map(response=>response.json())
              .catch(this.handleError)
  }
  get(slug){
      return this.http.get(endpoint)
              .map(response=>{
                  let data=response.json().filter(item=>{
                      if(item.slug==slug){
                          return item
                      }
                  })
                  // console.log(data)
                  if(data.length==1){
                      return data[0]
                  }
                    return {}
              })
              .catch(this.handleError)
  }

  search(query){
      return this.http.get(endpoint)
              .map(response=>{
                  let data=[]
                  let req=response.json().filter(item=>{
                      if(item.name.indexOf(query)>=0){
                          data.push(item)
                      }
                  })
                  console.log("search() data: in trip.service.ts",data)
                  return data
              })
              .catch(this.handleError)
  }

}
