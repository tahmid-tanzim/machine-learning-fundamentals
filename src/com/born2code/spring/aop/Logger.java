package com.born2code.spring.aop;

import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {

    /* reusablePointCut */
    @Pointcut("within(com.born2code.spring.aop.*)")
    public void withinDemo() {
    }

    /* reusablePointCut */
    @Pointcut("target(com.born2code.spring.aop.Camera)")
    public void targetDemo() {
    }

    /* reusablePointCut */
    @Pointcut("this(com.born2code.spring.aop.ICamera)")
    public void thisDemo() {
    }

    @Before("withinDemo()")
    public void withinBeforeDemo() {
        System.out.println("*********** WITHIN DEMO *********");
    }

    @Before("targetDemo()")
    public void targetBeforeDemo() {
        System.out.println("*********** Target DEMO *********");
    }

    @Before("thisDemo()")
    public void thisBeforeDemo() {
        System.out.println("*********** This DEMO *********");
    }
}
