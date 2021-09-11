import { Component, OnInit } from '@angular/core';
declare const MODULE_UL: any;

@Component({
  selector: 'menu',
  templateUrl: './section.component.html',
  styleUrls: ['./section.component.scss']
})
export class SectionComponent implements OnInit {
  
  constructor() { 
  }
  
  ngOnInit(): void {
    var links = new MODULE_UL("titles");
    links.addLink("Test", null);
    links.addLink("Test", "http://google.com");
    links.addLink("Test", null)
    links.sousLink("coucou","none");
  }

}
