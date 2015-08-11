package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component
public class Car {
    public void run() {
        System.out.println("Nice Car");
    }
}
