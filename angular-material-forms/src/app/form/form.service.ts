import { Observable } from "rxjs/internal/Observable"
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError } from "rxjs/internal/operators/catchError";
import { of } from "rxjs/internal/observable/of";
import { throwError } from "rxjs/internal/observable/throwError";

@Injectable({
    providedIn: 'root'
})
export class FormService {
    url = "http://localhost:8000/api/word-count/";
    options: { headers: HttpHeaders} = {headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*'
    })}
    
    constructor(private http: HttpClient) { 
        this.options.headers.append('Content-Type', 'application/json');
    }

    count_backend(text: string | null, option: number): Observable<any> {
        const formText = text !== null ? text : "";
        const info = {
            form_text: formText,
            option: option
        }
        return this.http.post<any>(this.url, info,this.options)
        .pipe(
            catchError(err => {
                console.error('Error:', err);
                return throwError('Something went wrong with the request.');
            })
        );
    }
}


