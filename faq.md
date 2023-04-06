# FAQ

## Εγκατάσταση Nextcloud

### Λείπει το Ansible module `mysql`

Από την έκδοση 2.10 του Ansible και μετά, στην εγκατάσταση του Ansible
περιλαμβάνεται και το collection `community.mysql`, που είναι όντως
προαπαιτούμενο. Εκδόσεις παλιότερες της 2.10 δεν υποστηρίζονται πλέον
από την Ansible. Παρακαλούμε αναβαθμίστε το Ansible.

### Παρουσιάζεται σφάλμα κατά την εκτέλεση του task που κάνει reboot

Αυτό συμβαίνει όταν το target machine είναι το localhost, όταν δηλαδή
χρησιμοποιείται ως Ansible controller το ίδιο μηχάνημα στο οποίο θέλουμε
να εγκαταστήσουμε το Nextcloud. Αυτό δεν υποστηρίζεται.

### Γιατί ferm;

Γρήγορη απάντηση: Γιατί είναι καλύτερο και απλούστερο.

Εκτενέστερη απάντηση: Επειδή το iptables είναι δύσκολο στη χρήση, πολλοί
χρήστες χρησιμοποιούν ufw. Αν και συχνά κάνει τη δουλειά, το ufw είναι
υπερβολικά απλό. Μπορεί να δουλεύει καλά για χρόνια και κάποια στιγμή θα
χρειαστείτε κάτι που δεν κάνει. Π.χ. μπορεί να θέλετε να κλείσετε την
πρόσβαση σε συγκεκριμένη IP. Αυτός ο κανόνας πρέπει να είναι απ' τους
πρώτους που θα εκτελεστούν, και στο ufw είναι δύσκολο να ορίσεις τη
σειρά των κανόνων (τουλάχιστον με το Ansible).

Με το ferm, όλο το configuration του firewall είναι σε αρχεία μέσα στο
/etc/ferm. Ένα απλό `service ferm reload` αντικαθιστά όλα τα iptables με
αυτά που προσδιορίζονται στο /etc/ferm. Το `service ferm stop`
απενεργοποιεί το firewall. Η σύνταξη των αρχείων είναι απλή και
ευέλικτη, με αποτέλεσμα το ferm να είναι τελικά και πιο εύκολο από άλλα,
αν και αυτό εξαρτάται βέβαια από την εμπειρία που έχει καθένας.

Το ferm το προτιμούν και άλλοι, όπως για παράδειγμα το debops project.

Για περισσότερες πληροφορίες για τη χρήση του ferm στο Ansible, βλέπε το
ρόλο [common](https://github.com/aptiko-ansible/common).