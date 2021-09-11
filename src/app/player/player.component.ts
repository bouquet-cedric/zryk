import { Component, Input, OnInit, Self } from '@angular/core';
declare const tAudio: String[];
declare const convert;

@Component({
  selector: 'player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit {
  
  play_pause:String="stop";
  num:number=0;
  AUDIO: HTMLAudioElement;
  volume:number=0.5;
  constructor() {
  }

  ngOnInit(): void {
    document.getElementById("temps").style.display="none";
    var div = document.getElementById('vol');
    var inp = document.getElementsByTagName("input")
    document.getElementById("titre").textContent = <string>tAudio[0].split(".")[0];
    for (let i in inp)
    {
      if (inp[i].id == "volume")
      {
        div.textContent=inp[i].value+" %";
        inp[i].style.backgroundColor="lightgreen";
        inp[i].addEventListener('change',function(aud)
        {
          var val = inp[i].value;
          div.textContent= val +" %";
          var real = parseInt(val);
          if (real == 100)
          {
            inp[i].style.backgroundColor="red";
          }
          else if (real >= 80)
          {
            inp[i].style.backgroundColor="orange";
          }
          else if (real >= 60)
          {
            inp[i].style.backgroundColor="yellow";
          }
          else if (real >= 40)
          {
            inp[i].style.backgroundColor="lightgreen";
          }
          else if (real >= 20)
          {
            inp[i].style.backgroundColor="royalblue";
          }
          else
          {
            inp[i].style.backgroundColor="purple";
          }
        });
      }
    }
  }

  affect()
  {
    var div =  <HTMLInputElement>document.getElementById("volume");
    this.volume = parseInt(div.value)/100;
    console.log("VOLUME = "+this.volume);
    if (this.play_pause != "stop") this.AUDIO.volume = this.volume;
  }

  
  
  play()
  {
    console.log(this.play_pause);
    if (this.play_pause == "stop" || this.play_pause == "pause")
    {
      if (this.play_pause == "stop")
      {
        if (tAudio.length > this.num)
        {
          var titre = tAudio[this.num].split(".")[0];
          document.getElementById("titre").textContent=<string>titre;
          this.AUDIO = new Audio("../../assets/audios/"+tAudio[this.num]);
          this.AUDIO.volume=this.volume;
          this.AUDIO.addEventListener("timeupdate",function()
          {
            var barre_temps = <HTMLProgressElement>document.getElementById("temps");
            barre_temps.style.display="block";
            var d = document.getElementById("time");
            var tps = convert(this.currentTime);
            var end = convert(this.duration);
            d.textContent = tps+" / "+end;
            barre_temps.value = this.currentTime;
            barre_temps.max = this.duration;
          });
          this.AUDIO.play();
          this.play_pause = "play";
        }
      }
      else
      {
        this.AUDIO.play();
        this.play_pause = "play";
      }
    }
    else if (this.play_pause == "play")
    {
      if (this.AUDIO.duration > this.AUDIO.currentTime)
      {
        this.play_pause = "pause";
        this.AUDIO.pause();
      }
      else
      {
        this.play_pause = "stop";
        this.play();
      }
    }
  }

}
