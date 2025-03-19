#include <stdio.h>
#include <string.h>
#include <ctype.h>

int verifier_mot_de_passe(const char *mdp) {
    int longueur = strlen(mdp);
    int majuscule = 0, minuscule = 0, chiffre = 0, special = 0;

    // Caractères spéciaux autorisés
    char special_chars[] = "@#$%&*!";

    // Vérifier la longueur
    if (longueur < 8) {
        printf("❌ Mot de passe trop court (min. 8 caractères)\n");
        return 0;
    }

    // Vérification des conditions
    for (int i = 0; i < longueur; i++) {
        if (isupper(mdp[i])) majuscule = 1;
        if (islower(mdp[i])) minuscule = 1;
        if (isdigit(mdp[i])) chiffre = 1;
        if (strchr(special_chars, mdp[i])) special = 1;
    }

    // Vérifier si toutes les conditions sont remplies
    if (majuscule && minuscule && chiffre && special) {
        printf("✅ Mot de passe valide\n");
        return 1;
    } else {
        printf("❌ Mot de passe non sécurisé :\n");
        if (!majuscule) printf("   - Il manque une majuscule\n");
        if (!minuscule) printf("   - Il manque une minuscule\n");
        if (!chiffre) printf("   - Il manque un chiffre\n");
        if (!special) printf("   - Il manque un caractère spécial (@#$%&*!)\n");
        return 0;
    }
}

int main() {
    char mot_de_passe[100];

    printf("Entrez un mot de passe : ");
    scanf("%s", mot_de_passe);

    verifier_mot_de_passe(mot_de_passe);

    return 0;
}

