import { TestBed, inject } from '@angular/core/testing';

import { TripService } from './trips.service';

describe('TripService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TripService]
    });
  });

  it('should be created', inject([TripService], (service: TripService) => {
    expect(service).toBeTruthy();
  }));
});
