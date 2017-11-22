import { Component, OnInit } from '@angular/core';
import { DinosaurService } from '../../services/dinosaurService'

@Component({
  selector: 'dinosaurs',
  template: './dinosaurs.html',
  // template: `<ul><li *ngFor="let dino of dinos">{{dino.site_name}}</li></ul>` // works

})
export class DinosaurComponent implements OnInit {
  dinos: any[];
  error: any;

  constructor(private dinosaurService: DinosaurService) { }

  getDinos() {
    this.dinosaurService
        .getDinos()
        .then(dinos => this.dinos = dinos)
        .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getDinos();
  }
}
