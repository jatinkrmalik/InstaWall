import { Component, OnInit } from '@angular/core';
import { PolygonService } from './polygon.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'installwall';
  screenWidth: any;
  screenHeight: any;
  randomColor: any;
  randomStroke: any;
  type: string;
  polyPoints = ``;
  response: any;
  randomStrokeWidth: number;

  constructor(
    private polyService: PolygonService
  ) { }

  ngOnInit() {
    this.screenHeight = window.innerHeight;
    this.screenWidth = window.innerWidth;
  }

  getPatterns() {
    this.generateRandomPolygon();
    this.getColors();
  }

  getColors() {
    this.randomColor = this.getHexCodes();
    this.randomStroke = 'transparent';
  }

  getHexCodes() {
    this.randomStrokeWidth = Math.random() * (+40 - +1) + + 1;
    return '#' + '0123456789abcdef'.split('').map(function (v, i, a) {
      return i > 5 ? null : a[Math.floor(Math.random() * 16)];
    }).join('');
  }

  generateRandomPolygon() {
    const a = {x: 0, y: 0}, b = {x: 0, y: 0} , c = {x: 0, y: 0};
    const random = (max, min) => Math.random() * (+max - +min) + + min;
    let polyArr = '';

    function nextPoly() {

    }

    this.polyService.getPolyCordinates(this.screenWidth, this.screenHeight).subscribe(
      (res) => {
        console.log(res);
        this.response = res;
        console.log(this.response.plotMe[0][0]);
        this.type = res['type'];
        if (this.type === 'polygon') {
          polyArr = '';
        res['plotMe'].map(tupple => {
          polyArr = `${polyArr} ${tupple[0]},${tupple[1]} `;
        });

        this.polyPoints = polyArr;
        }
      });
  }
}
