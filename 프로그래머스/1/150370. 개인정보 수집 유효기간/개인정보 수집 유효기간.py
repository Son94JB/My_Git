def solution(today, terms, privacies):
    answer = []
    term_aranged = []

    for i in range(len(terms)):
        term_type, expire = terms[i].split(" ")
        term_aranged.append((term_type, float(expire)))

    for i in range(len(privacies)):
        for detail_term in term_aranged:
            if detail_term[0] != privacies[i][-1]:
                continue

            term_month = int(detail_term[1])
            terms_year = 0
            if term_month >= 12:
                terms_year += term_month//12
                term_month -= terms_year*12

            start_year = int(privacies[i][:4])
            start_month = int(privacies[i][5:7])
            start_day = int(privacies[i][8:10])

            year = start_year + terms_year
            month = start_month + term_month
            day = start_day

            if month > 12:
                year += 1
                month -= 12

            today_year = int(today[:4])
            today_month = int(today[5:7])
            today_day = int(today[8:10])

            if today_year > year:
                answer.append(i+1)

            if today_year == year and today_month > month:
                answer.append(i+1)

            if today_year == year and today_month == month and today_day >= day:
                answer.append(i+1)

    return answer