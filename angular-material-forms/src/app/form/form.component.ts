import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms'; 
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { FormService } from './form.service';

interface FormInfo {
  title: string;
  value: string;
}

@Component({
  selector: 'app-form',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
     CommonModule,
    ReactiveFormsModule
  ],
    templateUrl: './form.component.html',
  styleUrls: ['./form.component.scss'],
})
export class FormComponent implements OnInit {

  @Output() formSubmitted = new EventEmitter<FormInfo>();  // New emitter

  form_info = [{
    "title": "Regex - Backend",  
    "value": '',
    }, 
    {"title": "Regex - Frontend",
    "value": '',
    }, 
    {"title": "Split - Backend",
    "value": '',
    }, 
    {"title": "Split - Frontend",
    "value": '',
    }
  ]
  word_count_form: FormControl<any> = new FormControl('');
  formControls!: FormControl<string | null>[];
  word_count_value = [0, 0, 0, 0]

  
  constructor(private http_service: FormService) {}
  ngOnInit(): void {
    this.formControls = this.form_info.map(info => new FormControl(''));
  }

  submitForm(index: number) {
    switch (this.form_info[index].title) {
      case "Regex - Backend":
        this.http_service.count_backend(this.formControls[index].value, 0).subscribe( count_number => {
          this.word_count_value[index] = count_number
        })
        break;
      case "Split - Backend":
        this.http_service.count_backend(this.formControls[index].value, 1).subscribe( count_number => {
          this.word_count_value[index] = count_number
        })
        break;
      case "Regex - Frontend":
        this.word_count_value[index] = this.count_regex(this.formControls[index].value)
        break;
      case "Split - Frontend":
        this.word_count_value[index] = this.count_split(this.formControls[index].value)
        break;
      default:
        this.count_regex(this.formControls[index].value)
        break;
    }
    return this.word_count_value[index]
  };

  count_regex(text: string | null): number{
    const match = Array.from(text!.matchAll(/\w+/g))
    return match?.length
  }
  
  count_split(text: string | null): number{
    const splited = text!.split(" ")
    return splited.length
  }
}
