import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CategoryListComponent } from './category-list.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NO_ERRORS_SCHEMA } from '@angular/core';

describe('CategoryListComponent', () => {
  let component: CategoryListComponent;
  let fixture: ComponentFixture<CategoryListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CategoryListComponent],
      imports: [HttpClientTestingModule], // Importa módulo para testes do HttpClient
      schemas: [NO_ERRORS_SCHEMA], // Ignora elementos desconhecidos no HTML
    }).compileComponents();

    fixture = TestBed.createComponent(CategoryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
