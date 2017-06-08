import { Component, OnInit } from '@angular/core';
import {SolverService} from '../../services/solver.service';

@Component({
  selector: 'app-solvers',
  templateUrl: './solvers.component.html',
  styleUrls: ['./solvers.component.css'],
  providers: [SolverService]
})
export class SolversComponent implements OnInit {

  file: File;
  inputValues: string;
  solvers: object[];
  selectedSolver: number;
  isCnf: boolean;

  loading: boolean;
  error: any;
  response: string;

  constructor(private solverService: SolverService) {
    this.loading = false;
    this.error = null;
    this.response = null;
    this.isCnf = true;
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

  onFileUpload(event) {
    this.file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      const text = reader.result;
      this.updateInputValues(text);
    };
    reader.readAsText(this.file);
  }

  private updateInputValues(inputValues) {
    this.inputValues = inputValues;
  }

  private handleRequest() {
    this.error = null;
    this.toggleLoading();
    this.solverService.calculate(this.inputValues, this.selectedSolver, this.isCnf).then(res => {
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
