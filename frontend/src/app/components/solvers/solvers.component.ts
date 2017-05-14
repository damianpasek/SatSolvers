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
  solvers: any[];
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
  }

  onFormSubmit() {
    this.loading = true;
    this.solverService.calculate(this.inputValues, this.selectedSolver).then(data => {
      data = data.json();
      this.response = data;
      this.loading = false;
    }).catch(err => {
      this.loading = false;
      this.error = err;
    });
  }

}
