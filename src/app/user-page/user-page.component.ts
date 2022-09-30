import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import {FormControl, Validators} from '@angular/forms';

// interface Target {
//   value: string;
//   viewValue: string;
// }

interface Period {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.css']
})
export class UserPageComponent implements OnInit {
  

  //target = new FormControl<Target | null>(null, Validators.required);
  period = new FormControl<Period | null>(null, Validators.required);



  // targets: Target[] = [
  //   {value: 'sales-0', viewValue: 'Sales'},
  //   {value: 'other-1', viewValue: 'Other'},
  // ];

  periods: Period[] = [
    {value: '0', viewValue: '1 Year'},
    {value: '1', viewValue: '2 Years'},
    {value: '2', viewValue:'4 Years'},
  ];

  @ViewChild('fileSelect') myInputVariable?: ElementRef;
  
  filename: any;
  format: any;
  formfile: any;
  file:any;
  showLoader: boolean = false;
  value: any;
  status: boolean=false;
  formdata: any;
  uploaded: boolean = false;
  name: any;


  constructor(
    private _snackBar: MatSnackBar,
    private http: HttpClient,
    private router:Router,
  ) { }
  
  
  onFileSelect(event: any) {
    try {
       this.file = event.target.files[0];
      if (this.file) {
        this.filename = this.file.name;
        this.format = this.file.name.split('.');
        // this.format = this.format[1];
        if (this.format[1] != 'csv') {
          this._snackBar.open("Please select only CSV file", "Close", { duration: 3000 });
          this.deleteFile();
        } else {
          this.formfile = new FormData();
          this.formfile.append('file', this.file);
          console.log("🎯TC🎯 ~ file: file-upload.component.ts ~ line 41 ~ this.formfile", this.formfile);
          this.uploaded=true;
        }
      }
    } catch (error) {
      this.deleteFile();
      console.log('no file was selected...');
    }
  }
  fileUpload() {
    if (this.file) {
      this.showLoader = true;
      let url = "http://localhost:5000/api/file_upload"
      this.http.post(url, this.formfile).subscribe((res) => {
        this.showLoader = false;
        this._snackBar.open("File successfully uploaded", "Ok", { duration: 5000 });
        this.status= false;
        this.router.navigate(['/predict']);
      },
        (error) => {
          this.showLoader = false;
          this._snackBar.open(error.message, "Close", { duration: 5000 });
        });
    }else{
      this._snackBar.open("Please select the file", "Ok", { duration: 3000 });
    }
    

  }


  ngOnInit(): void {
    
  }

  updateCategory(){
    let url = "http://localhost:5000/api/file_upload"
    this.http.post(url,this.value).subscribe
    console.log(this.value)
  }

  deleteFile(){
    this.file = null;
    this.format = null;
    this.filename = null;
    this.formfile.delete('file');
    // this.fileSelect
  }


}
