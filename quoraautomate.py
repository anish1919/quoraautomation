from selenium import webdriver 
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
driver = webdriver.Chrome(r'D:\Chromedriver\chromedriver.exe') #D:\Chromedriver
driver.get("https://quora.com") 

#driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input").send_keys(Keys.ENTER)
try:
    driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys("") # Enter quora email-id within the quotes ("") to automatically enter e-mail during login
except:
    pass

def inp():
    arr=['https://www.quora.com/Should-Rajvardhan-Hangargekar-get-to-play-for-CSK-instead-of-Mukesh-Choudhary-Why', 'https://www.quora.com/Would-it-be-a-good-choice-to-privatize-Coal-India-in-or-after-August-2022-Why', 'https://www.quora.com/What-is-the-best-performance-by-Eknath-Solkar-in-international-cricket', 'https://www.quora.com/How-did-the-Harshad-Mehta-saga-change-the-Indian-stock-markets', 'https://www.quora.com/What-are-some-bugs-in-the-remote-desktop-application-AnyDesk', 'https://www.quora.com/What-happens-in-Java-if-two-threads-of-the-same-priority-is-called-to-execute-a-task', 'https://www.quora.com/How-exactly-does-throttling-help-prevent-cascading-failures-that-an-lead-to-a-massive-outage', 'https://www.quora.com/unanswered/Why-is-Linux-considered-by-software-developers-as-the-favourite-environment-for-industrial-automation-and-robotics', 'https://www.quora.com/What-is-the-correlation-between-personal-expenditure-levels-and-inflation-rates-in-economies', 'https://www.quora.com/Does-using-a-different-lens-affect-the-dynamic-range-for-HDR-post-processing', 'https://www.quora.com/unanswered/What-are-some-organizations-particularly-software-that-reward-recognize-hard-work-instead-of-rewarding-only-the-results', 'https://www.quora.com/unanswered/Is-it-a-good-long-term-bet-to-invest-in-RateGain-shares-Why', 'https://www.quora.com/Is-it-possible-for-Reliance-Industries-stock-to-hit-5000-Why', 'https://www.quora.com/What-is-the-most-efficient-piece-of-code-to-find-out-the-longest-common-subarray-among-the-given-arrays', 'https://www.quora.com/How-exactly-does-insertion-sort-execute-faster-than-selection-sort', 'https://www.quora.com/What-are-some-insurance-issues-faced-by-bikes-having-more-than-150cc-engine-capacity', 'https://www.quora.com/What-can-be-done-in-India-when-someone-crashes-a-parked-car-and-the-impact-of-the-crash-pushed-the-car-into-a-no-parking-zone-and-the-car-owner-gets-a-ticket-for-no-parking', 'https://www.quora.com/Is-Lokesh-Kanagaraj-the-next-big-director-in-Tamil-cinema-Why', 'https://www.quora.com/unanswered/How-exactly-is-throttling-useful-to-prevent-a-DDoS-attack', 'https://www.quora.com/What-is-the-fastest-way-to-find-out-the-total-number-of-possibilities-to-choose-two-numbers-from-a-list-such-that-the-sum-of-those-numbers-is-equal-to-6', 'https://www.quora.com/How-exactly-did-Spring-Boot-make-it-easier-to-deploy-web-applications-in-an-embedded-servlet-container', 'https://www.quora.com/Why-is-it-suggested-to-safely-eject-a-pen-drive-before-removing-it-from-a-PC', 'https://www.quora.com/How-exactly-is-fast-jwt-is-faster-than-jsonwebtoken', 'https://www.quora.com/Why-is-the-Windows-OS-referred-to-as-bloated-spyware-by-many-developers', 'https://www.quora.com/Does-Indian-Railways-have-the-expertise-to-carry-out-mega-projects-like-Bilaspur-Manali-Leh-railway-line-Why', 'https://www.quora.com/Is-it-possible-to-fully-cover-a-square-with-7-rectangles-such-that-every-rectangle-has-a-2-1-ratio-no-part-of-any-rectangle-is-outside-the-square-and-no-two-rectangles-overlap', 'https://www.quora.com/Why-is-it-said-that-stock-markets-ignoring-negative-news-is-a-classic-sign-of-a-bullish-market', 'https://www.quora.com/Why-does-it-always-feel-more-comfortable-to-ride-pillion-in-motorbikes-within-125-cc-range-than-in-motorcycles-above-150cc-range', 'https://www.quora.com/What-are-some-examples-of-the-usage-of-document-forms-0-submit-in-JavaScript', 'https://www.quora.com/What-exactly-is-the-difference-between-window-confirm-and-confirm-in-JavaScript', 'https://www.quora.com/What-is-your-review-of-the-2022-Tamil-movie-Diary', 'https://www.quora.com/Does-Dixon-Technologies-have-further-potential-as-a-multibagger-Why', 'https://www.quora.com/How-are-lighthouses-able-to-reflect-light-for-long-distances', 'https://www.quora.com/Why-is-it-suggested-to-not-use-binary-search-when-a-given-list-is-not-sorted', 'https://www.quora.com/Why-is-China-facing-an-economic-crisis-in-August-2022', 'https://www.quora.com/What-is-your-review-of-the-2022-Tamil-movie-Maaran', 'https://www.quora.com/What-are-Dinesh-Karthiks-chances-to-get-selected-in-the-Indian-squad-for-the-ICC-T20-World-Cup-2022-after-his-performance-in-the-IPL-2022', 'https://www.quora.com/What-should-India-do-to-look-forward-to-discover-a-cure-for-Type-2-diabetes-considering-the-high-occurrence-and-vulnerability-of-the-condition-in-Indians', 'https://www.quora.com/unanswered/What-are-the-steps-to-increase-the-Memcached-default-size-for-object-storage-from-64MB-to-256MB-in-a-Windows-based-memcache-server', 'https://www.quora.com/What-are-some-key-pointers-while-designing-software-systems', 'https://www.quora.com/unanswered/What-are-MySQL-databases-more-vulnerable-to-SQL-injections', 'https://www.quora.com/Why-is-it-suggested-to-not-use-spaces-in-file-and-directory-names-in-Linux', 'https://www.quora.com/What-is-the-scope-of-Java-in-product-based-companies', 'https://www.quora.com/What-happens-when-data-redundancy-is-introduced-into-a-normalized-database-design', 'https://www.quora.com/unanswered/Is-it-effective-to-make-backups-immutable-and-stored-on-AWS-S3-in-a-serialized-format-Why', 'https://www.quora.com/Is-it-true-that-Robin-Uthappa-wouldve-made-it-bigger-if-he-was-provided-more-support-and-opportunities-at-international-level-Why', 'https://www.quora.com/unanswered/What-are-the-ways-in-which-Apollo-Tyres-can-maintain-a-balance-between-cost-cuts-and-price-hikes', 'https://www.quora.com/How-has-the-Nifty-FII-flow-dynamic-changed-in-recent-years', 'https://www.quora.com/Is-there-any-correlation-between-sugar-levels-and-consumption-of-bitter-gourd-Why', 'https://www.quora.com/What-is-the-difference-between-db-collection-find-name-eq-Australia-and-db-collection-find-name-Australia-in-MongoDB', 'https://www.quora.com/unanswered/Is-Soft-Suave-Technologies-Pvt-Ltd-Chennai-a-good-company-to-join-as-a-software-engineer-trainee-for-freshers-having-freelance-and-internship-experience-Why', 'https://www.quora.com/What-is-your-review-of-the-2022-Kannada-movie-Sugarless', 'https://www.quora.com/What-is-the-reason-behind-Samsung-M31-constantly-freezing-for-a-few-minutes-How-can-this-problem-be-fixed', 'https://www.quora.com/What-are-some-debt-free-multibagger-stocks-to-consider-investing-in-during-and-after-2022', 'https://www.quora.com/unanswered/What-are-some-future-technology-multi-bagger-stocks-to-buy-every-dip-on-and-after-August-2022', 'https://www.quora.com/unanswered/Are-Federal-Bank-shares-worth-a-buy-after-the-Q1-earnings-in-2022-Why', 'https://www.quora.com/unanswered/What-is-the-technical-explanation-for-why-Archive-Utility-can-throws-the-error-that-it-could-not-be-opened-while-unzipping-certain-apps-while-Keka-third-party-archive-software-worked-perfectly-for-the-same-purpose', 'https://www.quora.com/What-are-some-useful-tips-for-a-slow-learner-who-aims-to-become-a-web-developer', 'https://www.quora.com/unanswered/Is-Web3-login-authentication-better-than-Web2-login-Why', 'https://www.quora.com/Is-Ethereum-a-blockchain-or-not-Why', 'https://www.quora.com/Is-it-recommended-to-invest-in-KPIT-shares-despite-high-valuation-Why', 'https://www.quora.com/How-should-a-student-respond-when-a-professor-answers-doubts-with-Its-obvious', 'https://www.quora.com/What-could-be-the-reasons-behind-emails-showing-up-in-the-sent-folder-in-Gmail-but-the-recipient-did-not-receive-the-sent-email', 'https://www.quora.com/How-will-the-acquisition-of-Exide-Life-by-HDFC-Life-affect-the-policyholders-existing-policy-s-terms-and-conditions', 'https://www.quora.com/unanswered/Why-does-the-TVS-Raider-have-oxygen-sensor-problems', 'https://www.quora.com/Who-are-some-successful-people-in-history-who-are-known-to-be-slow-workers-slow-learners', 'https://www.quora.com/What-is-the-psychology-behind-dogs-loving-squeaky-toys', 'https://www.quora.com/How-exactly-is-recursion-useful-in-solving-the-data-structure-problem', 'https://www.quora.com/What-are-some-ways-to-prevent-the-HTTP-429-error-in-a-website', 'https://www.quora.com/Is-a-medium-sized-papaya-suitable-to-be-consumed-after-breakfast-Why', 'https://www.quora.com/What-are-the-advantages-of-RDBMS-over-a-simple-custom-DBMS', 'https://www.quora.com/Why-are-springs-not-used-as-an-energy-source-for-cell-phones', 'https://www.quora.com/If-force-depends-only-on-mass-and-acceleration-how-come-faster-objects-deal-more-damage', 'https://www.quora.com/Is-it-true-that-a-meritorious-dictatorship-is-better-compared-to-a-cesspit-democracy-Why', 'https://www.quora.com/HTML-Why-do-we-define-start-attribute-in-ordered-list', 'https://www.quora.com/What-is-the-science-behind-the-practice-of-blowing-a-conch-shankh-during-daily-prayers', 'https://www.quora.com/Is-the-Honda-SP-125-a-good-bike-for-Indian-roads-Why', 'https://www.quora.com/unanswered/In-the-AnyDesk-application-the-message-Remote-AnyDesk-client-is-offline-Trying-to-wake-it-up-by-Wake-On-Lan-pops-up-when-connecting-to-another-PC-using-AnyDesk-How-exactly-does-Wake-On-Lan-work-in-this-scenario']
    for i in arr:
        driver.get(i)
        sleep(3)
        driver.find_element_by_css_selector("#mainContent > div.q-box.qu-borderAll.qu-borderRadius--small.qu-borderColor--raised.qu-boxShadow--small.qu-bg--raised > div > div > div > div.q-box.qu-zIndex--action_bar > div > div > div > div:nth-child(1) > button:nth-child(3) > div > div.q-text.qu-display--inline-flex.qu-alignItems--center.qu-overflow--hidden.puppeteer_test_button_text.qu-medium.qu-color--gray.qu-ellipsis.qu-ml--tiny > div").click()
        sleep(4)
        try:
            open()
        except:
            continue
    link1(arr)
    print(req)
    

def type(click):
    for i in range(9,29):
        if click<25:
            try:
                driver.find_element_by_css_selector("#selector-option-"+str(i)+" > div > div > div.q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium > div > div > div > span > span > svg > g > circle").click()
                click+=1
                print(click)
            except:
                continue
        if click==26:
            click()

def open():
    i=2
    click = 0
    while click < 25:
        try:
            a = "#root > div > div:nth-child(2) > div > div > div > div > div.q-flex.ModalContainerInternal___StyledFlex-s8es4q-2.gXhqYs.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-box.qu-overflowY--auto > div.q-flex.qu-pt--small.qu-justifyContent--center > div:nth-child(2) > div > div > div > div > div.q-box > div:nth-child(2) > div:nth-child("+str(i)+") > div > div > div > div.q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium > div > div > div > span > span > svg"
            #a = "#root > div > div:nth-child(2) > div > div > div > div > div.q-flex.ModalContainerInternal___StyledFlex-s8es4q-2.gXhqYs.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-box.qu-overflowY--auto > div.q-flex.qu-pt--small.qu-justifyContent--center > div:nth-child(2) > div > div > div > div > div.q-box > div:nth-child(2) > div:nth-child("+str(i)+") > div > div > div > div.q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium > div > div > div > span > span > svg"
            driver.find_element_by_css_selector(a).click()
            click += 1
            i += 1
            #req+=1
            print(click)
            driver.execute_script("window.scrollBy(0,8)", "")
        except:
            i += 1
            continue
            return
            
if __name__ == "__main__":
    try:
        inp()
    except:
        inp()
