#define ledPin 13

String serverIn = "";
bool stringComplete = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serverIn.reserve(1024);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (stringComplete){
    if ((serverIn == "ON") || (serverIn == "on") || (serverIn == "On") ){
      Serial.println("Turn On");
      digitalWrite(ledPin, HIGH); 
    }
    else if ((serverIn == "OFF") || (serverIn == "off") || (serverIn == "Off")){
      Serial.println("Turn Off");
      digitalWrite(ledPin, LOW); 
    }
    else{
      Serial.println("Unknown command");
    }
    serverIn = "";
    stringComplete = false; 
  }
}

void serialEvent(){
  while (Serial.available()){
    char inChar = (char)Serial.read();
    if (inChar == '\n'){
      stringComplete = true;
    }else{
      serverIn += inChar;
    }
    delay(5);
  }
}
