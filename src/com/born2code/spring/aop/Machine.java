package com.born2code.spring.aop;


public class Machine implements IMachine {
    @Override
    public void start() {
        System.out.println("Machine starting ...");
    }
}
