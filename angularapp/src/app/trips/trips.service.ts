import { Injectable } from '@angular/core';
import {Http} from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';


const endpoint='assets/json/trips.json'

@Injectable()
export class TripService {
  data:[any];
  private apiURL = 'http://localhost:8000/api/places-travelplan/';
  constructor(private http:Http) { }

  listTrips() {
    return this.http.get(this.apiURL)
              .toPromise()
              .then(response => response.json())
              .catch(this.handleError_getdinos);
  }

  // listPlaces(){
  //   return this.http.get(this.apiURL)
  //             .map(response=>{
  //                 this.data=response.json().filter(item=>{
  //                  console.log("listplaces. services: all", item.site_city_parent)
  //                     if(this.data.indexOf(item.site_city_parent)==-1){
  //                         this.data.push(item.site_city_parent)
  //                         console.log("pushing..",item.site_city_parent)
  //                     }
  //                 })
  //                 console.log("in listPlaces: cities",this.data)
  //                 return this.data
  //             })
  //             .catch(this.handleError)

  // }

  detailTrips(slug){
    return this.http.get(this.apiURL)
              .map(response=>{
                  let data=response.json().filter(item=>{
                    // console.log("filtering..","item-site-slug:",item.site_slug,"slug",slug)
                      if(item.site_slug==slug){
                          return item
                      }
                  })
                  console.log("in get - service: data",data)
                  if(data.length==1){
                      return data[0]
                  }
                    return {}
              })
              .catch(this.handleError)
  }
  list(){ // only for carousel..
      return this.http.get(endpoint)   // to avoid needing to subscribe/unsubscribe:use map+catch
              .map(response=>response.json())
              .catch(this.handleError)
  }
  get(slug){
      return this.http.get(this.apiURL)
              .map(response=>{
                  let data=response.json().filter(item=>{
                    console.log("filtering..","item-site-slug:",item.site_slug,"slug",slug)
                      if(item.site_slug==slug){
                          return item
                      }
                  })
                  console.log("in get - service: data",data)
                  if(data.length==1){
                      return data[0]
                  }
                    return {}
              })
              .catch(this.handleError)
  }
  search(query){
    // query=query.replace(/\W/g, '').toLowerCase()
    query=query.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();})
    console.log("new query:", query)
      return this.http.get(this.apiURL)
              .map(response=>{
                  let data=[]
                  let req=response.json().filter(item=>{
                    // console.log("filtering..",item)

                      if(item.site_name.indexOf(query)>=0){
                          data.push(item)
                      }
                      if(item.site_city_parent.indexOf(query)>=0){
                          data.push(item)
                      }
                      if(item.site_category.indexOf(query)>=0){
                          data.push(item)
                      }
                      if(item.site_state.indexOf(query)>=0){
                          data.push(item)
                      }
                      // can add more if statements to add cetgories/city/other fields..
                  })
                  console.log("search() data: in trip.service.ts",data)
                  return data
              })
              .catch(this.handleError)
  }


  private handleError_getdinos(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
  private handleError(error:any, caught:any):any{
          console.log(error,caught)
  }
}

