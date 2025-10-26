import collections

class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"Teacher(name='{self.first_name} {self.last_name}', age={self.age}, subjects={self.can_teach_subjects})"

def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule_teachers = []
    teacher_assignments = collections.defaultdict(set)

    while uncovered_subjects:
        best_teacher = None
        max_covered = -1

        for teacher in teachers:
            newly_covered = teacher.can_teach_subjects.intersection(uncovered_subjects)
            num_newly_covered = len(newly_covered)

            if num_newly_covered > max_covered:
                max_covered = num_newly_covered
                best_teacher = teacher
            elif num_newly_covered == max_covered and num_newly_covered > 0:
                 if best_teacher is None or teacher.age < best_teacher.age:
                     best_teacher = teacher

        if max_covered == 0 or best_teacher is None:
            return None

        assigned_subjects_now = best_teacher.can_teach_subjects.intersection(uncovered_subjects)
        uncovered_subjects.difference_update(assigned_subjects_now)
        best_teacher.assigned_subjects.update(assigned_subjects_now)

        if best_teacher not in schedule_teachers:
            schedule_teachers.append(best_teacher)

    return schedule_teachers

if __name__ == '__main__':
    all_subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers_data = [
        ("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        ("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        ("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        ("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        ("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        ("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'}),
    ]
    teachers = [Teacher(*data) for data in teachers_data]
    schedule = create_schedule(all_subjects, teachers)

    if schedule:
        print("Розклад занять успішно складено (покриття множини):")
        print("--------------------------------------------------")
        covered_subjects = set()
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}")
            covered_subjects.update(teacher.assigned_subjects)
        print("--------------------------------------------------")
        print(f"Усі предмети: {', '.join(sorted(all_subjects))}")
        print(f"Покриті предмети: {', '.join(sorted(covered_subjects))}")

        if all_subjects.issubset(covered_subjects):
             print(f"\nКритерій 1 виконано: Покриті всі {len(covered_subjects)} предмети.")
        else:
             print("\nКритерій 1 НЕ виконано: Не всі предмети покриті.")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
        print("Критерій 2 виконано: Виведено повідомлення про неможливість покриття.")