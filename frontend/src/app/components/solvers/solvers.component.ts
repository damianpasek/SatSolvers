import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-solvers',
  templateUrl: './solvers.component.html',
  styleUrls: ['./solvers.component.css']
})
export class SolversComponent implements OnInit {

  inputValues: string;
  solvers: any[];
  selectedSolver: number;

  constructor() { }

  ngOnInit() {
  }

  onFormSubmit() {
    console.log(this.inputValues);
  }

}
