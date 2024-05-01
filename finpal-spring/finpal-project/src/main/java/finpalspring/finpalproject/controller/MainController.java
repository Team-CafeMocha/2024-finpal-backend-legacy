package finpalspring.finpalproject.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {
    @GetMapping("/home")
    public String mainPage() {
        return "homepage";  // mainpage.html을 반환
    }

}
