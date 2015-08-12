package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component
public class Fan implements IFan {
    @Override
    public void activate(int level) {
        System.out.println("Fan running at level: " + level);
    }
}
