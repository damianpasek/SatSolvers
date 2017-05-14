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

  constructor(private solverService: SolverService) { }

  ngOnInit() {
  }

  onFormSubmit() {
    this.solverService.calculate(this.inputValues, this.selectedSolver).then(data => {
      console.log(data);
    }).catch(err => {
      console.log('Error: ', err);
    });
  }

}
