#define FORWARDS 1
#define BACKWARDS 0

int powerR = 3;
int powerL = 11;
int dirR = 12;
int dirL = 13;
int currentR = 0;
int currentL = 1;

void setup(){
  Serial.begin(9600);
  pinMode(powerR, OUTPUT);
  pinMode(powerL, OUTPUT);
  pinMode(dirR, OUTPUT);
  pinMode(dirL, OUTPUT);
}


void cease(int duration){
  digitalWrite(powerR, LOW);
  digitalWrite(powerL, LOW);
  delay(duration); 
}

void backwards(int duration){
  digitalWrite(dirR, BACKWARDS);
  digitalWrite(dirL, BACKWARDS);
  digitalWrite(powerR, HIGH);
  digitalWrite(powerL, HIGH);
  delay(duration);
}

void forwards(int duration){
  digitalWrite(dirR, FORWARDS);
  digitalWrite(dirL, FORWARDS);
  digitalWrite(powerR, HIGH);
  digitalWrite(powerL, HIGH);
  delay(duration);
}

void rotate(int duration, char course){
  if (course == 'r'){
    digitalWrite(dirR, BACKWARDS);
    digitalWrite(dirL, FORWARDS);
  }
  else {if (course == 'l'){
    
    digitalWrite(dirR, FORWARDS);
    digitalWrite(dirL, BACKWARDS);
  }}

  digitalWrite(powerR, HIGH);
  digitalWrite(powerL, HIGH);
  delay(duration);
}

void loop(){
  char input = Serial.read();
  if (input == 'f') forwards(0);
  if (input == 'b') backwards(0);
  if (input == 'r') rotate(0, 'r');
  if (input == 'l') rotate(0, 'l');
  if (input == 's') cease(0);
}



