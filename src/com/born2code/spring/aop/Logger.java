package com.born2code.spring.aop;

import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {

    @Pointcut("execution(void com.born2code.spring.aop.Camera.snap())")
    public void reusablePointCut(){}

    @Before("reusablePointCut()")
    public void aboutToTakePhoto() {
        System.out.println("About To Take Photo...");
    }

    @After("reusablePointCut()")
    public void theEnd() {
        System.out.println("Bye...");
    }
}
