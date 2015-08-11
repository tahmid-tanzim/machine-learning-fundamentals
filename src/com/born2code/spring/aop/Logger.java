package com.born2code.spring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {

    /* reusablePointCut */
    @Pointcut("within(com.born2code.spring.aop.Camera)")
    public void cameraSnap() {
    }

    @Before("cameraSnap()")
    public void aboutToTakePhoto() {
        System.out.println("Before Advice - About To Take Photo...");
    }
}
