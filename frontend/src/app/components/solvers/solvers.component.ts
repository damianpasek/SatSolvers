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

  constructor(private solverService: SolverService) { }

  ngOnInit() {
  }

  onFormSubmit() {
    console.log('Request started...');
    this.solverService.calculate(this.inputValues, this.selectedSolver).then(data => {
      data = data.json();
      console.log(data);
      console.log('Request completed...');
    }).catch(err => {
      console.log('Error: ', err);
    });
  }

}
