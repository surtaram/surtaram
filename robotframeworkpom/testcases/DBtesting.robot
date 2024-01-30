*** Settings ***
Library     DatabaseLibrary
Library     OperatingSystem


Suite Setup     Connect To Database     pymysql     ${DBname}   ${DBuser}   ${DBpass}   ${DBhost}   ${DBport}
Suite Teardown      Disconnect From Database







*** Variables ***

${DBname}   mydb
${DBuser}   root
${DBpass}   root
${DBhost}   127.0.0.1
${DBport}   3306








