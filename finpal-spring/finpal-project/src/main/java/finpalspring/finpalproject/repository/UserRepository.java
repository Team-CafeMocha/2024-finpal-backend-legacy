package finpalspring.finpalproject.repository;

import finpalspring.finpalproject.domain.SiteUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<SiteUser, Long> {
}