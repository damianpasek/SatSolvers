import { Component, OnInit } from '@angular/core';
import {SolverService} from '../../services/solver.service';

@Component({
  selector: 'app-solvers',
  templateUrl: './solvers.component.html',
  styleUrls: ['./solvers.component.css'],
  providers: [SolverService]
})
export class SolversComponent implements OnInit {

  inputValues: string;
  solvers: object[];
  selectedSolver: number;

  loading: boolean;
  error: any;
  response: string;

  constructor(private solverService: SolverService) {
    this.loading = false;
    this.error = null;
    this.response = null;
  }

  ngOnInit() {
    this.solverService.getSolvers().subscribe(data => {
      this.solvers = data;
    });
  }

  onFormSubmit() {
    if (this.selectedSolver && this.inputValues !== '') {
      this.handleRequest();
    } else {
      this.error = 'You should fill form';
    }
  }

  private handleRequest() {
    this.error = null;
    this.toggleLoading();
    this.solverService.calculate(this.inputValues, this.selectedSolver).then(res => {
      res = res.json();
      this.response = res.data;
      this.toggleLoading();
    }).catch(err => {
      this.toggleLoading();
      this.error = err;
    });

  }

  private toggleLoading() {
    this.loading = !this.loading;
  }

}
