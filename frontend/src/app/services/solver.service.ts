import { Injectable } from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';
import {environment} from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class SolverService {

  constructor(private http: Http) { }

  getSolvers() {

  }

  calculate(input: string, solver: number): Promise<any> {
    const headers = new Headers({ 'Content-Type': 'application/json' });
    const options = new RequestOptions({headers});
    const body = { input, solver };

    return this.http.post(environment.apiUrl, JSON.stringify(body), options).toPromise();
  }
}
