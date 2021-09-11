import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'clic',
  templateUrl: './clic.component.html',
  styleUrls: ['./clic.component.scss']
})
export class ClicComponent implements OnInit {
  
  clic:boolean = false;
  duree:string = '0.5s';
  constructor() {
  }
  
  ngOnInit(): void {
  }
  
  private entree(id :string)
  {
    var elt = document.getElementById(id);
    elt.classList.remove("animate__animated", "animate__slideOutLeft");
    elt.classList.add("animate__animated", "animate__slideInLeft");
    elt.style.setProperty('--animation-duration', this.duree);
  }
  
  private moveLeft(id :string)
  {
    var elt = document.getElementById(id);
    elt.classList.remove("animate__animated", "animate__slideInRight");
    elt.classList.add("animate__animated", "animate__slideInLeft");
    elt.style.setProperty('--animation-duration', this.duree);
  }
  
  private sortie(id: string)
  {
    var elt = document.getElementById(id);
    elt.classList.remove("animate__animated", "animate__slideInLeft");
    elt.classList.add("animate__animated", "animate__slideOutLeft");
    elt.style.setProperty('--animation-duration', this.duree);
  }
  
  private moveRight(id: string)
  {
    var elt = document.getElementById(id);
    elt.classList.remove("animate__animated", "animate__slideInLeft");
    elt.classList.add("animate__animated", "animate__slideInRight");
    elt.style.setProperty('--animation-duration', this.duree);
  }
  
  
  exec() {
    var elt = document.getElementById("switch");
    if (!this.clic)
    {
      this.entree("main");
      // this.moveLeft("switch");
      // elt.style.left="20%";
      this.clic = true;
      elt.style.cursor="url(\"../../assets/minus2.CUR\"), default";
      elt.title="hide menu";
    }
    else
    {
      this.sortie("main");
      // this.moveRight("switch");
      // elt.style.left="0";
      this.clic = false;
      elt.style.cursor="url(\"../../assets/pilus2.CUR\"), default";
      elt.title="show menu";
    }
  }
}
