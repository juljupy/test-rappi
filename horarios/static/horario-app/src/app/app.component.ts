import { Component } from '@angular/core';
import { CalendarComponent } from './calendar.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  entryComponents: [CalendarComponent]
})

export class AppComponent{

}