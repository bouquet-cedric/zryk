import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ClicComponent } from './clic.component';

describe('ClicComponent', () => {
  let component: ClicComponent;
  let fixture: ComponentFixture<ClicComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ClicComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ClicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
