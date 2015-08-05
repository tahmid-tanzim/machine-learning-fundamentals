package com.born2code.spring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {

    /* reusablePointCut */
    @Pointcut("execution(* com.born2code.spring.aop.Camera.*(..))")
    public void cameraSnap() {
    }

    @Before("cameraSnap()")
    public void aboutToTakePhoto() {
        System.out.println("About To Take Photo...");
    }

    @After("cameraSnap()")
    public void afterAdvice() {
        System.out.println("After Advise...");
    }

    @AfterReturning("cameraSnap()")
    public void afterReturning() {
        System.out.println("After Returning");
    }

    @AfterThrowing("cameraSnap()")
    public void afterThrowing() {
        System.out.println("After Throwing");
    }

    @Around("cameraSnap()")
    public void aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) {
        System.out.println("--- Around Advice (Before) ---");

        try {
            proceedingJoinPoint.proceed();
        } catch (Throwable throwable) {
            System.out.println("in Around Advice: " + throwable.getMessage());
        }

        System.out.println("--- Around Advice (After) ---");
    }
}
