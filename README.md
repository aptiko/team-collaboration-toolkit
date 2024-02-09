# Ασφαλές λογισμικό για συνεργασία

[Documentation for the Ansible collections](https://team-collaboration-toolkit.readthedocs.io/)

Γρήγορη μετάβαση: [Απαιτήσεις](https://github.com/grnet/team-collaboration-toolkit#%CE%B1%CF%80%CE%B1%CE%B9%CF%84%CE%AE%CF%83%CE%B5%CE%B9%CF%82) | [Εγκατάσταση](https://github.com/grnet/team-collaboration-toolkit#%CE%B5%CE%B3%CE%BA%CE%B1%CF%84%CE%AC%CF%83%CF%84%CE%B1%CF%83%CE%B7) | [Εκπαίδευση/υποστήριξη](https://github.com/grnet/team-collaboration-toolkit#%CE%B5%CE%BA%CF%80%CE%B1%CE%AF%CE%B4%CE%B5%CF%85%CF%83%CE%B7-%CE%BA%CE%B1%CE%B9-%CF%85%CF%80%CE%BF%CF%83%CF%84%CE%AE%CF%81%CE%B9%CE%BE%CE%B7) | [Γνωστά προβλήματα](https://github.com/grnet/team-collaboration-toolkit#%CE%B3%CE%BD%CF%89%CF%83%CF%84%CE%AC-%CF%80%CF%81%CE%BF%CE%B2%CE%BB%CE%AE%CE%BC%CE%B1%CF%84%CE%B1)

## Εισαγωγή

Οι κυβερνήσεις και δημόσιοι οργανισμοί απομακρύνονται τα τελευταία
χρόνια από τους ιδιώτες παρόχους cloud υπηρεσιών εν μέσω αυξανόμενων
ανησυχιών σχετικά με την ψηφιακή κυριαρχία, την ιδιωτικότητα και την
ασφάλεια. Αυτοί οι λόγοι έχουν οδηγήσει στην αναζήτηση λύσεων ανοιχτού
λογισμικού που μπορούν να εγκατασταθούν στην υποδομή ενός οργανισμού
(self-hosted) ενώ ταυτόχρονα διαθέτουν τις απαραίτητες λειτουργίες που
προσφέρουν οι εμπορικές υπηρεσίες όπως π.χ. το Google Workspace και το
Microsoft 365.

Εδώ υλοποιούμε υπό τη μορφή εργαλειοθήκης (toolkit) μια ολοκληρωμένη
λύση ή αλλιώς ένα **Ασφαλές Περιβάλλον Συνεργασίας** με βάση τα
λογισμικά [Nextcloud](https://nextcloud.com/),
[Collabora](https://www.collaboraoffice.com/),
[Matrix](https://matrix.org/), [Element](https://element.io/) και
[Jitsi](https://jitsi.org/). Το Nextcloud διαθέτει ολοκληρωμένο
περιβάλλον με λειτουργίες όπως η αποθήκευση και ο διαμοιρασμός αρχείων,
email, ημερολόγιο, συνομιλίες κ.ά. Το Collabora είναι σουίτα
συνεργατικής επεξεργασίας εγγράφων η οποία ενσωματώνεται στο Nextcloud.
Τα Matrix και Element είναι εφαρμογές ασφαλούς επικοινωνίας και
συνεργασίας και το Jitsi πλατφόρμα τηλεδιασκέψεων.

Τα παραπάνω λογισμικά δεν είναι φυσικά οι μοναδικές επιλογές, αλλά
επιλέχθηκαν γιατί αποτελούν διαδεδομένες λύσεις που χρησιμοποιούνται ήδη
με επιτυχία από κυβερνητικούς οργανισμούς παγκοσμίως, βρίσκονται σε
συνεχή ανάπτυξη, υποστηρίζονται και συνεισφέρουν σε αυτά μεγάλες
κοινότητες και διαθέτουν ειδικά πακέτα υποστήριξης για εταιρείες και
οργανισμούς.

## Γιατί αυτό το toolkit

Τα οφέλη ενός οργανισμού που θα επιλέξει το Ασφαλές Περιβάλλον Εργασίας
είναι πολλά. Εκτός από την ελαχιστοποίηση του κόστους, με αυτό ένας
κυβερνητικός οργανισμός εξασφαλίζει την **ψηφιακή του κυριαρχία**, την
**ασφάλεια και προστασία των δεδομένων** και επιτρέπει την **ψηφιακή
μετάβαση** τους.

### Ψηφιακή κυριαρχία

Η ψηφιακή κυριαρχία (digital sovereignty) αναφέρεται στην ικανότητα
κάποιου να ασκεί έλεγχο στα δικά του δεδομένα και την ψηφιακή του
υποδομή, διασφαλίζοντας ότι δεν υπόκειται σε εξωτερική επιρροή ή
επιτήρηση. Με την ανάπτυξη αυτο-εξυπηρετούμενης λύσης, οι δημόσιοι
φορείς μπορούν να έχουν μεγαλύτερο έλεγχο των δεδομένων τους, καθώς αυτά
βρίσκονται στη δική τους υποδομή και δεν αποθηκεύονται σε διακομιστές
που διαχειρίζονται ιδιώτες πάροχοι υπηρεσιών. Η προσέγγιση αυτή
επιτρέπει στις κυβερνήσεις να ενισχύσουν την ψηφιακή τους κυριαρχία και
να μετριάσουν τους πιθανούς κινδύνους που συνδέονται με την ανάθεση
ευαίσθητων δεδομένων σε υπηρεσίες τρίτων.

### Ασφάλεια και προστασία των δεδομένων των πολιτών

Με την αυξανόμενη ψηφιοποίηση, η πρόκληση της προστασίας της ιδιωτικής
ζωής και της ασφάλειας γίνεται ολοένα και μεγαλύτερη. Οι κυβερνήσεις
διαχειρίζονται ευαίσθητες πληροφορίες των πολιτών και είναι ζωτικής
σημασίας να διασφαλιστεί η εμπιστευτικότητα, η ακεραιότητα και η
διαθεσιμότητα αυτών των δεδομένων.

Τα λογισμικά του toolkit διαθέτουν διάφορα χαρακτηριστικά και πρακτικές
που συμβάλλουν στην προστασία των δεδομένων των πολιτών, όπως η
κρυπτογράφηση δεδομένων, ο έλεγχος πρόσβασης, εποπτεία και καταγραφή.
Προσφέρουν επίσης χαρακτηριστικά και πρακτικές που ευθυγραμμίζονται με
τους κανονισμούς προστασίας δεδομένων, όπως ο Γενικός Κανονισμός για την
Προστασία Δεδομένων της Ευρωπαϊκής Ένωσης (GDPR). Παρέχουν εργαλεία που
βοηθούν τις κυβερνήσεις να εκπληρώσουν τις νομικές τους υποχρεώσεις όσον
αφορά την προστασία των δεδομένων, συμπεριλαμβανομένων χαρακτηριστικών
όπως οι πολιτικές διατήρησης δεδομένων και η φορητότητα δεδομένων.

Με τη χρήση αυτών των χαρακτηριστικών, οι κυβερνητικοί οργανισμοί
μπορούν να δημιουργήσουν ισχυρό πλαίσιο προστασίας δεδομένων, που
διασφαλίζει ότι τα δεδομένα των πολιτών παραμένουν εμπιστευτικά και δεν
είναι επιρρεπή σε διαρροές ή μη εξουσιοδοτημένη πρόσβαση.

### Η ανάγκη της ψηφιοποίησης

Στη σημερινή εποχή κυβερνητικοί οργανισμοί χρειάζεται να ανέβουν επίπεδο
και να βελτιώσουν την παραγωγικότητα, επιτρέποντας την εξ αποστάσεως
εργασία, τη συνεργασία σε πραγματικό χρόνο και τη γρήγορη αλλά ασφαλή
ανταλλαγή εγγράφων με άλλους οργανισμούς. Το Ασφαλές Περιβάλλον
Συνεργασίας παρέχει μια ολοκληρωμένη πλατφόρμα που διευκολύνει διάφορες
πτυχές της διαδικασίας ψηφιακού μετασχηματισμού.

Το Nextcloud υποστηρίζει την απομακρυσμένη εργασία και την κινητικότητα,
επιτρέποντας στους κυβερνητικούς υπαλλήλους να έχουν πρόσβαση στα
αρχεία, τα έγγραφα και τις εφαρμογές τους από οποιαδήποτε τοποθεσία και
συσκευή. Αυτή η ευελιξία ενισχύει την παραγωγικότητα, την ισορροπία
μεταξύ επαγγελματικής και προσωπικής ζωής και τη συνέχεια των
κυβερνητικών λειτουργιών, ιδίως κατά τη διάρκεια απροσδόκητων γεγονότων,
όπως φυσικές καταστροφές ή καταστάσεις έκτακτης ανάγκης στον τομέα της
δημόσιας υγείας.

Τα Nextcloud, Matrix/Element και Jitsi προσφέρουν εργαλεία επικοινωνίας
και συνεργασίας, συμπεριλαμβανομένων λειτουργιών διάσκεψης ήχου/βίντεο,
άμεσων μηνυμάτων και ομαδικής συνομιλίας. Αυτές οι λειτουργίες
επιτρέπουν στους κυβερνητικούς υπαλλήλους να επικοινωνούν και να
συνεργάζονται αποτελεσματικά, είτε εργάζονται εξ αποστάσεως είτε εντός
κυβερνητικών γραφείων. Η απρόσκοπτη επικοινωνία και συνεργασία
συμβάλλουν στην ενίσχυση της ομαδικής εργασίας, την ταχύτερη λήψη
αποφάσεων και τη βελτίωση της αποτελεσματικότητας των κυβερνητικών
λειτουργιών.

## Απαιτήσεις

### Άνθρωποι

Καταρχήν χρειάζεται να υπάρχει ένας διαχειριστής συστημάτων ο οποίος θα
εγκαταστήσει τα συστήματα. Χρειάζεται γνώση σε ansible και docker. Ο
χρόνος που πρέπει να αφιερώσει για να έχει το πλήρες σύστημα έτοιμο
εκτιμάται σε μερικές μέρες (με την προϋπόθεση ότι υπάρχει γνώση σε
ansible και docker), χωρίς να περιλαμβάνεται το backup (επειδή ο κάθε
οργανισμός έχει διαφορετικές πρακτικές ως προς το backup, οι λύσεις που
παρέχονται εδώ δεν περιλαμβάνουν backup—περιλαμβάνονται όμως οδηγίες ως
προς το τι θα πρέπει να γίνει backup).

Χρειάζεται επίσης ένας άνθρωπος ο οποίος γνωρίζει ή θα μάθει τα
συστήματα απ' την πλευρά του χρήστη και θα προσφέρει εκπαίδευση και
υποστήριξη στους χρήστες.

### Υλικό

Χρειάζονται δύο (τουλάχιστον) server (καλό είναι το Nextcloud να
βρίσκεται σε διαφορετικό server απ' ό,τι τα Matrix/Element και Jitsi).
Γενικά για 50 χρήστες ένας server για το Nextcloud και ένας για τα
υπόλοιπα θα πρέπει να αρκεί. Περισσότερες πληροφορίες για τη
διαστασιολόγηση των server αναφέρονται παρακάτω.

Είναι προφανές ότι για να εξασφαλίζεται ο πλήρης έλεγχος των δεδομένων
οι server πρέπει να βρίσκονται σε χώρο της εταιρείας. Η εγκατάσταση σε
server φιλοξενούμενους από πάροχο μπορεί εντούτοις να δώσει μέρος των
πλεονεκτημάτων, όπως ανεξαρτησία (π.χ. δυνατότητα μετακόμισης σε άλλο
πάροχο) και εξασφάλιση του απορρήτου στην ανταλλαγή μηνυμάτων και στις
βιντεοκλήσεις, αφού τα Matrix και Jitsi υποστηρίζουν κρυπτογράφηση
end-to-end.

#### Nextcloud

Περίληψη: Για 50 χρήστες: 4 επεξεργαστές, 8 GB RAM, και χώρος στο δίσκο
όσο χρειάζονται οι χρήστες για τα αρχεία τους, συν 30 GB. Αυτά τα
ενδεικτικά νούμερα είναι με επιφύλαξη—διαβάστε αναλυτικά παρακάτω.

Στην ΕΔΥΤΕ όπου το Nextcloud χρησιμοποιείται επί του παρόντος από 50
χρήστες, το έχουμε εγκατεστημένο σε virtual servers που έχουν ιδιαίτερα
αργούς δίσκους, με αποτέλεσμα η ταχύτητα του δίσκου να είναι το
bottleneck. Για να αντιμετωπίσουμε αυτό το πρόβλημα, έχουμε βάλει τη
MySQL σε χωριστό virtual server, και αυτός ο χωριστός virtual server
έχει δύο διαφορετικούς δίσκους: έναν για τα redo logs κι έναν για τα
data files. Με αυτό τον τρόπο χρησιμοποιούμε τρεις δίσκους παράλληλα.
Όμως σε ένα server με σύγχρονους δίσκους (πολύ περισσότερο σε ένα server
με SSD), είναι απίθανο να χρειαστεί κάτι τέτοιο.

Ο server του Nextcloud που χρησιμοποιούμε έχει 16 CPU και 32 GB RAM, απ'
ό,τι βλέπουμε όμως τα CPU κάθονται, υπάρχουν 20 GB RAM ελεύθερα και 9 GB
που χρησιμοποιούνται για buffers+cache. Στο μηχάνημα με τη mysql είναι
δύσκολο να μιλήσουμε για RAM γιατί ούτως ή άλλως η mysql καταναλώνει όλη
τη διαθέσιμη, πάντως και πάλι τα 8 CPU κάθονται. Η εκτίμησή μας από αυτό
που βλέπουμε είναι ότι, αν είχαμε γρηγορότερο δίσκο, θα επαρκούσε ένας
server με τις προδιαγραφές που αναφέραμε στην περίληψη παραπάνω.

Όμως το πόσο ζορίζεται το μηχάνημα εξαρτάται και από το τι χρήση κάνουν
αυτοί οι 50 χρήστες, και σίγουρα κάθε οργανισμός είναι διαφορετικός.
Στην περίπτωσή μας, οι μισοί περίπου είναι developers/devops που
χρησιμοποιούν το Nextcloud ελάχιστα, αφού κατά κύριο λόγο δουλεύουν σε
editors και gitlab. Για το δικό σας οργανισμό δεν ξέρουμε, αλλά είναι
πιθανό ούτε εσείς να ξέρετε πριν εγκατασταθεί το σύστημα και το δείτε
στην πράξη.

Σε χώρο δίσκου, βλέπουμε ότι το εγκατεστημένο σύστημα και η MySQL με τα
δεδομένα της καταλαμβάνουν λίγο πάνω από 10 GB, αλλά η MySQL θα
διογκώνεται αργά καθώς περνά ο καιρός. Θεωρούμε λοιπόν ότι 30 GB που
προτείνουμε είναι περίπου το διπλάσιο απ' ό,τι χρειάζεται και θα
καταλήξει σε κατανάλωση χώρου περίπου 50%. Αυτό όμως το νούμερο δεν
περιλαμβάνει τα αρχεία των χρηστών.

#### Matrix/Element/Jitsi

Τα Matrix και Element έχουν μικρές απαιτήσεις. Γενικά 2 CPU, 2 GB RAM,
και 30 GB δίσκος πρέπει να αρκούν για τις περισσότερες χρήσεις.

Για το Jitsi οι απαιτήσεις εξαρτώνται από πολλούς παράγοντες: Πόσοι θα
είναι οι ταυτόχρονοι χρήστες και οι ταυτόχρονες τηλεσυσκέψεις, ποια θα
είναι η ποιότητα της εικόνας, και αν θα υπάρχει δυνατότητα εγγραφής των
τηλεσυσκέψεων, και πόσων τηλεσυσκέψεων ταυτόχρονα (το Jibri, δηλαδή το
component που πραγματοποιεί την εγγραφή, είναι ιδιαίτερα απαιτητικό).
Δεν υπάρχει λόγος να επαναλάβουμε εδώ τις [απαιτήσεις που
προδιαγράφονται στην τεκμηρίωση του
Jitsi](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-requirements/),
που είναι αναλυτικές.

Το component του Jitsi στο οποίο γίνονται οι τηλεσυσκέψεις λέγεται Jitsi
Video Bridge ή JVB. Μπορεί σε μία εγκατάσταση Jitsi να υπάρχουν πολλά
JVB, καθένα σε διαφορετικό server. Μία τηλεσύσκεψη γίνεται μόνο σε ένα
JVB, αλλά όταν γίνονται πολλές ταυτόχρονες συσκέψεις τότε γίνεται load
balancing στα υπάρχοντα JVB. Επομένως μπορεί να θέλετε να προβλέψετε
πολλά μηχανήματα με JVB ανάλογα με το τι περιμένετε. Το toolkit που
χρησιμοποιούμε έχει τον περιορισμό ότι το πρώτο JVB είναι στον ίδιο
server με τα Matrix και Element, όμως ο φόρτος που προκαλούν αυτά τα
δύο είναι αμελητέος σε σχέση με το Jitsi, επομένως αυτό δεν αναμένεται
να είναι πρόβλημα.

### Λειτουργικό σύστημα

Για το Nextcloud, επί του παρόντος υποστηρίζουμε μόνο Debian και Ubuntu.
Για τα Matrix, Element και Jitsi, οι απαιτήσεις σε λειτουργικό σύστημα
αναφέρονται στην αρχή της [τεκμηρίωσης του
toolkit](https://github.com/spantaleev/matrix-docker-ansible-deploy/blob/master/docs/prerequisites.md).

## Εγκατάσταση

### Nextcloud

Για την εγκατάσταση του Nextcloud έχουμε το Ansible collection
[grnet.nextcloud](https://grnetnextcloud.readthedocs.org/).

### Matrix, Element, Jitsi

Το Matrix είναι ένα πρωτόκολλο (ή σύνολο πρωτοκόλλων), όπως είναι το
email. Ο Matrix Synapse είναι ένας matrix server, όπως ο Postfix είναι
ένας email server. Τέλος, το Element είναι ένας Matrix client, που είναι
μάλιστα web client. Στο παράδειγμα με το email, το αντίστοιχο είναι το
Roundcube.

Για την εγκατάσταση των Matrix (ειδικότερα του Matrix Synapse), Element
και Jitsi χρησιμοποιούμε το δημοφιλές
[matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy).
Η τεκμηρίωσή του είναι εκτενής και παραπέμπουμε σ' αυτό για περισσότερα.
Ειδικότερα, για το Jitsi, είναι χρήσιμη και η [περιγραφή της
αρχιτεκτονικής](https://gitlab.grnet.gr/digigov-oss/ansible/jitsi-meet#jitsi-architecture)
σε ένα Jitsi Ansible module που δημιουργήσαμε παλιότερα (του οποίου τη
χρήση δεν προτείνουμε γιατί είναι ασυντήρητο).

## Εκπαίδευση και υποστήριξη

### Nextcloud

Για το Ansible collection grnet.nextcloud, υποστήριξη προσφέρει η ΕΔΥΤΕ
(και συγκεκριμένα ο δημιουργός των ρόλων, Αντώνης Χριστοφίδης,
achristofides@admin.grnet.gr).

Εκπαίδευση και υποστήριξη στους χρήστες σας θα πρέπει να προσφέρει ο
οργανισμός σας, δημιουργώντας μια ομάδα υποστήριξης. Η ΕΔΥΤΕ έχει
δημιουργήσει [εκπαιδευτικό
υλικό](https://howto.gov.gr/course/index.php?categoryid=7) με μαθήματα σε
βίντεο. Έχει σχεδιαστεί με επίκεντρο το χρήστη, και περιέχει
παραδείγματα και σενάρια χρήσης της καθημερινής εργασίας. Το υλικό
ενημερώνεται συχνά με κάθε νέα λειτουργία και αλλαγή στα εργαλεία του
toolkit.

Η Nextcloud GmbH προσφέρει υποστήριξη δεύτερου επιπέδου. Η συνήθης ροή
είναι ότι οι χρήστες ζητούν υποστήριξη από την ομάδα υποστήριξης του
οργανισμού. Για θέματα που δεν μπορεί να αντιμετωπίσει η ομάδα
υποστήριξης ρωτάει τους διαχειριστές συστημάτων. Ακολούθως, αν
χρειάζεται, οι διαχειριστές ζητάνε βοήθεια από την υποστήριξη της
Nextcloud.  Το σχετικό προϊόν ονομάζεται [Nextcloud
Enterprise](https://nextcloud.com/enterprise/), πρακτικά όμως είναι
απλώς τεχνική υποστήριξη, αφού ο κώδικας του Nextcloud Enterprise είναι
ακριβώς ο ίδιος με του Nextcloud Community. 

Αν δεν αγοράσετε υποστήριξη από τη Nextcloud, τότε μένουν τα ανεπίσημα
κανάλια, όπως εμείς (η ΕΔΥΤΕ), με όση εμπειρία έχουμε από τη χρήση που
κάνουμε, και το [forum του Nextcloud
community](https://help.nextcloud.com/categories).

### Matrix/Element/Jitsi

Για το matrix-docker-ansible-deploy υπάρχει [υποστήριξη από την
κοινότητα](https://github.com/spantaleev/matrix-docker-ansible-deploy#support).
Όσες φορές χρειαστήκαμε κάτι μας έδωσαν την απάντηση στο σχετικό matrix
room.

Όπως και στο Nextcloud, υποστήριξη στους χρήστες σας θα πρέπει να
προσφέρει μια ομάδα υποστήριξης του οργανισμού. Το εκπαιδευτικό υλικό
που αναφέραμε για το Nextcloud παραπάνω καλύπτει και τα
Matrix/Element/Jitsi. Σύμφωνα με την εμπειρία μας, τα Matrix, Element
και Jitsi λειτουργούν πιο απρόσκοπτα και οι λειτουργίες τους είναι πιο
προφανείς στους χρήστες, με αποτέλεσμα οι ανάγκες υποστήριξης να είναι
μικρότερες σε σχέση με το Nextcloud, ενώ και η υποστήριξη δεύτερου
επιπέδου (πέραν της ανεπίσημης από την κοινότητα) είναι λιγότερο
αναγκαία σε σχέση με το Nextcloud.

## Γνωστά προβλήματα

### Nextcloud

* Σε «διαμοιρασμένα» ημερολόγια, [δεν ενημερώνει τους συμμετέχοντες σε
  events](https://github.com/nextcloud/server/issues/26668).
* Παρόλο που δεν τους ενημερώνει, [ισχυρίζεται ότι τους
  ενημέρωσε](https://github.com/nextcloud/calendar/issues/4983).
* Όταν ο χρήστης έχει ανοιχτό το ημερολόγιο, [πρέπει να πατήσει
  ανανέωση](https://github.com/nextcloud/calendar/issues/31) για να
  φανούν αλλαγές που έχουν γίνει από άλλους χρήστες (ή από τον ίδιο
  χρήστη σε άλλες συσκευές).
* Ο συγχρονισμός του Nextcloud με το ημερολόγιο του Android είναι
  πολύπλοκος στην εγκατάσταση από το χρήστη.  Απαιτείται η εγκατάσταση
  της εφαρμογής DAVx⁵, για την οποία είτε ο χρήστης πρέπει να πληρώσει
  περίπου €5 στο Google Play είτε να εγκαταστήσει το F-Droid (που με τη
  σειρά του δεν είναι τόσο απλό στην εγκατάσταση όσο άλλες εφαρμογές που
  βρίσκονται στο Google Play) και στη συνέχεια να εγκαταστήσει το DAVx⁵
  απ' το F-Droid. Ακόμα κι αν δεν υπήρχε αυτή η δυσκολία, η [διαδικασία
  εγκατάστασης](https://docs.nextcloud.com/server/latest/user_manual/en/groupware/sync_android.html#contacts-and-calendar)
  είναι πολύπλοκη για τους περισσότερους χρήστες.

### Matrix/Element

* Ενοχλητικά [κόκκινα
  γράμματα](https://github.com/vector-im/element-meta/issues/744) στο
  Element.

### matrix-docker-ansible-deploy

* Δεν υποστηρίζει (ακόμα) [εγγραφή
  τηλεσυσκέψεων](https://github.com/spantaleev/matrix-docker-ansible-deploy/issues/1473).

## Περισσότερες πληροφορίες

* [Εγκατάσταση Nextcloud για τις ανάγκες ενός
  οργανισμού](https://opensource.ellak.gr/2021/05/03/nextcloud-installation-for-the-needs-of-an-organization/)
  (άρθρο Χρήστου Καραμολέγκου από Μάιο 2021).

## Άδεια χρήσης για το παρόν

© 2023 ΕΔΥΤΕ

Έχετε άδεια να αντιγράφετε, να διανέμετε και να τροποποιείτε το κείμενο
υπό τους όρους της άδειας χρήσης [CC BY-SA Greece
3.0](https://creativecommons.org/licenses/by-sa/3.0/gr/), και τα
παραδείγματα υπό τους όρους του [CC0
1.0](http://creativecommons.org/publicdomain/zero/1.0/).
