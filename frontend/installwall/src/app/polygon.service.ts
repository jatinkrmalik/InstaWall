import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PolygonService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getPolyCordinates(width: number, height: number) {
    return this.httpClient.get(`http://localhost:9090/generate/${width}/${height}`);
  }
}
