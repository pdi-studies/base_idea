import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrl: './category-list.component.css'
})
export class CategoryListComponent implements OnInit {
  categories: Array<any> = [];

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {}

  ngOnInit(): void {
    this.fetchCategories();
  }

  fetchCategories(): void {
    const apiUrl = 'http://localhost:5000/api/categories';
    this.http.get<Array<any>>(apiUrl).subscribe(
      (response) => {
        // Para cada categoria, converte o SVG em um SafeHtml
        this.categories = response.map((category) => {
          return {
            ...category,
            svg: this.sanitizer.bypassSecurityTrustHtml(category.icon), // Sanitiza o SVG
          };
        });
      },
      (error) => {
        console.error('Erro ao buscar categorias:', error);
      }
    );
  }

  getIcon(iconName: string): string {
    console.log('iconName: ', iconName);
    return `ph:${iconName}`;
  }

}
