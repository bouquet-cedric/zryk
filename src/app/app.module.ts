import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BarComponent } from './bar/bar.component';
import { SectionComponent } from './section/section.component';
import { ClicComponent } from './clic/clic.component';
import { PlayerComponent } from './player/player.component';
import { AlbumComponent } from './album/album.component';
import { DecorComponent } from './decor/decor.component';

@NgModule({
  declarations: [
    AppComponent,
    BarComponent,
    SectionComponent,
    ClicComponent,
    PlayerComponent,
    AlbumComponent,
    DecorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
