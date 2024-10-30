import 'dart:io';

String TreeConstructor(List strArr) {

  Map<String, int> parent = {};
  Map<String, int> child = {};

  for(var i = 0; i < strArr.length;i++){
    String str = strArr[i].substring(1,strArr[i].length - 1);
    List<String> numbers = str.split(',');

    final x = (parent[numbers[1]] ?? 0 ) + 1;
    final y = (child[numbers[0]] ?? 0 ) + 1;

    parent[numbers[1]] = x;
    child[numbers[0]]= y;
  
    if(y > 1 || x > 2){
      return 'false';
    }
  }
  return 'true';
}
